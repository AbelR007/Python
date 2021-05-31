# TOPIC : if __name__ is "__main__"
# Example of the __name__ conditional statement, and reasons why it is used?

class Name_Examples(object):
    """ Reasons for the use of __name__ :

    We use __name__ because it helps the code understand whether the file is run directly or is being imported to another file

    """
    def main():
        print("Code is being run directly")

    if __name__ == '__main__':
        main()
    else :
        print("Code is being imported to another file and being run from there.")

# Got more doubts, ask them in the Github Issues
# =========================================================
# CREATED with ❤️ by AbelR007
# =========================================================
