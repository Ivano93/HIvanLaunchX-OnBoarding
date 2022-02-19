def main():
    path = ("C:/Users/e7440/Documents/"
            "Launch X/Misiones - Launch X/"
            "Katas/KatasHIvanLaunchX-OnBoarding/"
            "Kata 10 - Módulo 10/config.txt")

    try:
        configuration = open(path)
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
    except IsADirectoryError:
                print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError as err:
                print("Found config.txt but couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()