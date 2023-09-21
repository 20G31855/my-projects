def main():
    while True:
        try:
            print(date_format(input("Date:")))
            break
        except:
            pass


# function returning the correct format
def date_format(calender):
    if calender.count("/")!= 0:
        month, date, year = calender.split("/")
        int_month = int(month)
        int_date = int(date)
        if int_date > 31:
            raise ValueError
        if int_month > 12:
            raise ValueError
        return(f"{year}-" + f"{int_month:02}-" + f"{int_date:02}")

    else:
        month, date, year = calender.split(" ")
        months = [
            "January","Febuary","March","April","May","June","July","August","September","October","November","December"
        ]
        #the valid date input for this format of date is preceeded with a ","
        days = [
            "1,","2,","3,","4,","5,","6,","7,","8,","9,"
        ]
        number = months.index(month)
        days_number = days.index(date)
        days_int = days_number+1
        month_int = number+1
        if days_int > 31:
            raise ValueError
        return(f"{year}-" + f"{month_int:02}-" + f"{days_int:02}")


main()