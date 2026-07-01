import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_obtener_todos_los_posts():
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 100
    print(f"✅ Se obtuvieron {len(posts)} posts correctamente")

def test_obtener_post_por_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert post["userId"] == 1
    assert "title" in post
    assert "body" in post
    print(f"✅ Post obtenido: {post['title'][:30]}...")

def test_crear_post():
    nuevo_post = {
        "title": "Test automatizado",
        "body": "Contenido del post de prueba",
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=nuevo_post)
    
    assert response.status_code == 201
    post_creado = response.json()
    assert post_creado["title"] == "Test automatizado"
    assert post_creado["userId"] == 1
    assert "id" in post_creado
    print(f"✅ Post creado con ID: {post_creado['id']}")

def test_actualizar_post():
    datos_actualizados = {
        "title": "Título actualizado",
        "body": "Contenido actualizado",
        "userId": 1
    }
    
    response = requests.put(f"{BASE_URL}/posts/1", json=datos_actualizados)
    
    assert response.status_code == 200
    post = response.json()
    assert post["title"] == "Título actualizado"
    print("✅ Post actualizado correctamente")

def test_eliminar_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    print("✅ Post eliminado correctamente")