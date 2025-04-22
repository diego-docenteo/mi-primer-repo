import sys
import subprocess
import datetime

def push_a_git():
    mensaje = f"Auto push desde Python ({datetime.datetime.now().isoformat(timespec='seconds')})"
    ruta_repo = "C:/Users/DiegoMartínez/OneDrive - docenteo.com/Git/mi-primer-repo"

    try:
        # Añadir cambios
        subprocess.run(["git", "-C", ruta_repo, "add", "."], check=True)

        # Hacer commit
        subprocess.run(["git", "-C", ruta_repo, "commit", "-m", mensaje], check=True)

        # Hacer push
        subprocess.run(["git", "-C", ruta_repo, "push", "origin", "main"], check=True)

        print("✅ Push automático completado.")

    except subprocess.CalledProcessError as e:
        print("❌ Error al hacer push automático:", e)

def main():
    
    print("Hola, mundo")

    push_a_git()

if __name__ == "__main__":
    main()