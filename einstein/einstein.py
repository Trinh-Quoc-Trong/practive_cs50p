def main():
    try:
        m =int(input("m: "))
    except ValueError:
        return
    
    c = 300000000
    e = m * (c ** 2)
    
    print(e)    

if __name__ == "__main__":
    main()