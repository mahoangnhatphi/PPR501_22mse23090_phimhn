import pymysql

from LaptopBestSeller import LaptopBestSeller
from Utils import to_int_value, is_best_seller


class Database:
    def connect(self):

        return pymysql.connect(host="localhost", user="root", password="password", database="laptop", charset='utf8mb4')

    def get_laptops_best_seller(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(
                "SELECT Id, Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller FROM laptopbestseller")
            data = cursor.fetchall()
            return [LaptopBestSeller(*laptop) for laptop in data]
        except:
            return ()
        finally:
            con.close()
        pass

    def get_laptop_by_id(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(
                "SELECT Id, Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller FROM laptopbestseller WHERE Id = %s",
                (id))
            laptop_best_seller = cursor.fetchone()
            return LaptopBestSeller(laptop_best_seller[0], laptop_best_seller[1], laptop_best_seller[2],
                                    laptop_best_seller[3], laptop_best_seller[4], laptop_best_seller[5],
                                    laptop_best_seller[6])
        except:
            return None
        finally:
            con.close()
        pass

    def insert(self, laptop_best_seller):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO laptopbestseller(Brand, Name, OldPrice, NewPrice, PercentDiscount, BestSeller) VALUES(%s, %s, %s, %s, %s, %s)",
                (laptop_best_seller.Brand, laptop_best_seller.Name, to_int_value(laptop_best_seller.OldPrice),
                 to_int_value(laptop_best_seller.NewPrice), to_int_value(laptop_best_seller.PercentDiscount),
                 is_best_seller(laptop_best_seller.BestSeller)))
            con.commit()

            return True
        except Exception as e:
            print("Failed to ", e)
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, laptop_best_seller):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE laptopbestseller set Brand = %s, Name = %s, "
                           "OldPrice = %s, NewPrice = %s, PercentDiscount = %s, BestSeller = %s where Id = %s",
                           (
                           laptop_best_seller.Brand, laptop_best_seller.Name, to_int_value(laptop_best_seller.OldPrice),
                           to_int_value(laptop_best_seller.NewPrice), to_int_value(laptop_best_seller.PercentDiscount),
                           is_best_seller(laptop_best_seller.BestSeller),
                           laptop_best_seller.Id))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, Id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM laptopbestseller where Id = %s", (Id))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
