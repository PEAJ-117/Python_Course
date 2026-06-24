if __name__ != "__main__":

    # from ..manage.crud import save # Import relative
    from users.manage.crud import save  # Import absolute

    print(__name__)

    def pay_taxes():
        print("Pagando impuestos")
        save()

if __name__ == "__main__":
    print("Mantenimiento")
