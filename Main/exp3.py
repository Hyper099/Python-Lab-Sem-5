import csv

def main():
    dict_fare = {}
    with open("../Data/passengers.csv", 'r') as f1, open("../Data/fare.csv", 'r') as f2, open("../Data/trains.csv", 'r') as f3 :
        passengerReader = csv.DictReader(f)
        fareReader = csv.DictReader(f)
        trainReader = csv.DictReader(f)

        for passenger in passengerReader:
            fare = 0
            passenger_name = passenger['Name']
            passenger_train_id = passenger['Train ID']
            tickets_req = passenger['Number of Tickers']
            
            for line in trainReader:
                if(passenger_train_id = line['Train ID'])
                    if(line['Total Seats'] > tickets_req){
                                        
                    }
            
        





if __name__ == "__main__":
    main()
