import random
import string

# Configuración
SERVER_URL = "http://c.3lok3.site:8080"
OUTPUT_FILE = "playlist.m3u"

def generate_random_credentials():
    """Genera credenciales únicas: dajaja + 5 dígitos aleatorios"""
    prefix = "dajaja"
    num = ''.join(random.choices(string.digits, k=5))
    return f"{prefix}{num}"

def build_m3u_content(username, password):
    """Construye un archivo M3U válido con la URL del servidor"""
    return f"""#EXTM3U
#EXTINF:-1,دجاجة سبورت
{SERVER_URL}/get.php?username={username}&password={password}&type=m3u
"""

def save_m3u_file(content, username, password, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Archivo M3U guardado: {filename}")
    print(f"🔗 URL del canal: {SERVER_URL}/get.php?username={username}&password={password}&type=m3u")

def main():
    print("🔄 Generando credenciales y lista M3U...")
    username = generate_random_credentials()
    password = username  # Mismo valor para usuario y contraseña
    m3u_content = build_m3u_content(username, password)
    save_m3u_file(m3u_content, username, password, OUTPUT_FILE)
    print(f"\n🎉 ¡Listo! Usa este archivo en tu página web.")
    print(f"⏳ Recuerda: esta URL expira en ~1.5 días. Vuelve a ejecutar este script para renovar.")

if __name__ == "__main__":
    main()