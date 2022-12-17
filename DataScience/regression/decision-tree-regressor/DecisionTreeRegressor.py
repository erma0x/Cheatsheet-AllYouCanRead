from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

   # SPLIT
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
   # BUILD MODEL
my_model = DecisionTreeRegressor()  Define model
   # FIT MODEL
my_model.fit(train_X, train_y)   Fit model

   # PREDICTION
val_predictions = melbourne_model.predict(val_X)    Get predicted prices on validation data

  #  MODEL ERROR 
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(val_y, val_predictions))  Print out error
    
   # OR
    
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
    
     #compare MAE with differing values of max_leaf_nodes

for max_leaf_nodes in [5, 50, 500, 5000]:        try different leaf_nodes 
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

best_tree_size is the number of nodes with less Error
    
   # Fit the model with best_tree_size. Fill in argument to make optimal size
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)

   #  fit the final model
final_model.fit(X, y)
