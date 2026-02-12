def main():
    greeting = input("File name: ").strip().lower()
    if greeting.endswith((".gif", ".jpeg", ".png")):
        print("image/" + greeting.split(".")[-1], end="")
    elif greeting.endswith((".pdf", ".zip")):
        print("application/" + greeting.split(".")[-1], end="")
    elif greeting.endswith(".txt"):
        print("text/plain", end="")
    elif greeting.endswith(".jpg"):
        print("image/jpeg", end="")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
