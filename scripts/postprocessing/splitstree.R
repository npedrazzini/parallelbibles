library(ape)
library(e1071)
library(phangorn)

# the df 'data' should already be in your environment: it's the first thing called with the script 'word-MDS.R'
 
data2 <- data[ ,-1]

data2 <- as.data.frame(t(data2))
data2[] <- lapply(data2, function(x) if(is.factor(x)) as.character(x) else x)

# Assign 1 to NULLs 0 to anything else
data2[data2=='NULL'] <- '1'
data2[data2!='1'] <- '0'
data2[is.na(data2) == TRUE] <- '0'

# Calculate Hamming distance between languages
matr2 <- as.matrix(data2)
hamm <- hamming.distance(matr2)

# Change to desired output path and name.nex

write.nexus.dist(hamm, file = "./NTonly.nex")

# Also try dendrogram (additionally)
# Starting from data2 as you reach it above

dist_mat <- dist(data2, method = 'euclidean')
hclust_avg <- hclust(dist_mat, method = 'average')
plot(hclust_avg, main = "Classif. by NULL-clause distribution")
rect.hclust(hclust_avg, border = 2:6)
