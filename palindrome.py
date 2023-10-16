def is_palindrome(r):
    # r იგულისხმება როგორც reversed
    r = r.replace(" ", "").lower()

    # r == r[::-1]-ის საშუალებით პროგრამა ამოწმებს არის თუ არა სიტყვა პალინდრომი
    if r == r[::-1]:
        print("yes")
    else:
        print("No")

# შეცვალეთ user_input  რათა ნახოთ შედეგი
user_input = "mom"
is_palindrome(user_input)