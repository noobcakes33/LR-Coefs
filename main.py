from function import fit_model1

if __name__ == "__main__":
    # defining our dataset file
    dataset = "Ass1.csv"
    # calling the fit_model1 function and passing the datset to it
    coef = fit_model1(data=dataset)
    # printing coefficients
    print(coef)
