def main():
    flavors = ["mint chocolate chip", "coffee", "french vanilla", "strawberry", "green tea",
               "chocolate chip cookie dough", "chocolate chip fudge brownie", "butter pecan"]
    choco = []
    for flavor in flavors:
        if "chocolate" in flavor:
            choco.append(flavor + " is the best!")
    print(choco)

    def tag_best(flavors_param):
        return flavors_param + " is the best!"
    def has_choco(flavors_param):
        return "chocolate" in flavors_param
    chocos = list(map(tag_best, list(filter(has_choco, flavors))))
    print(chocos)

    chocols = list(map(lambda x: x + " is the best!", list(filter(lambda y: "chocolate" in y, flavors))))
    print(chocols)

    chocolas = [flavor + " is the best!" for flavor in flavors if "chocolate" in flavor]
    print(chocolas)




if __name__ == "__main__":
    main()