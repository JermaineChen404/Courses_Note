square_me = function(n) {
  x=n*n
  return(x)
}

hello_there = function(name, adjective) {     
    phrase = paste("Hello ", name, "! You look ",                     
                    adjective,".", sep="")     
    print(phrase)  
} 

n = 5
x = numeric(n)
for (j in seq_len(n)) {
  x[j] = j^2
}
print(x)