from database import get_connection


def buscar_veiculos_controller():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, placa, modelo, cor, proprietario, status, imagem FROM veiculos")
    registros = cursor.fetchall()
    conn.close()

    veiculos = []
    for r in registros:
        veiculos.append({
            "id": r[0], "placa": r[1], "modelo": r[2],
            "cor": r[3], "proprietario": r[4], "status": r[5],
            "imagem": r[6]
        })
    return veiculos


def salvar_veiculo_controller(dados):
    conn = get_connection()
    cursor = conn.cursor()

    imagem_url = dados.get('imagem', '')

    query = """
        INSERT INTO veiculos (placa, modelo, cor, proprietario, status, imagem) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        dados['placa'],
        dados['modelo'],
        dados['cor'],
        dados['proprietario'],
        dados['status'],
        imagem_url
    )

    cursor.execute(query, valores)
    conn.commit()
    conn.close()


def deletar_veiculo_controller(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM veiculos WHERE id = %s", (id,))
    conn.commit()
    conn.close()

def buscar_veiculo_por_id_controller(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, placa, modelo, cor, proprietario, status, imagem FROM veiculos WHERE id = %s", (id,))
    r = cursor.fetchone()
    conn.close()

    if r:
        return {
            "id": r[0], "placa": r[1], "modelo": r[2],
            "cor": r[3], "proprietario": r[4], "status": r[5], "imagem": r[6]
        }
    return None


def atualizar_veiculo_controller(id, dados):
    conn = get_connection()
    cursor = conn.cursor()

    imagem_url = dados.get('imagem', '')

    query = """
                UPDATE veiculos 
                SET placa = %s, modelo = %s, cor = %s, proprietario = %s, status = %s, imagem = %s
                WHERE id = %s
            """
    valores = (
        dados['placa'],
        dados['modelo'],
        dados['cor'],
        dados['proprietario'],
        dados['status'],
        imagem_url,
        id
    )

    cursor.execute(query, valores)
    conn.commit()
    conn.close()