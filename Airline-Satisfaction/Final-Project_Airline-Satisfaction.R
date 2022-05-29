library(dplyr)
library(ggplot2)

head(air.sat)
summary(air.sat)
str(air.sat)



########################################################  
############################ Data Prep & Cleaning 
########################################################  

# rename columns 
air.sat <- air.sat %>% 
  rename(
    Loyalty = Customer.Type,
    Purpose = Type.of.Travel,
    Inflight.wifi = Inflight.wifi.service,
    Leg.room = Leg.room.service,
    Depart.Arrive.time.convenient = Departure.Arrival.time.convenient
  )

# Create age buckets 

air.sat$Age.Range <- ifelse(air.sat$Age < 25, "24 and under", 
  (ifelse(air.sat$Age < 40, "25-39", 
          (ifelse(air.sat$Age < 50, "40-49", "50 and over")))))

air.sat$Age.Bucket <- round(air.sat$Age, -1)

# Combine Eco and Eco Plus

air.sat$Class2 <- ifelse(air.sat$Class == "Business", "Business", "Economy")


# create new variable of overall Average of all ratings 
air.sat$Average.Rating <- (air.sat$Inflight.wifi + 
                             air.sat$Depart.Arrive.time.convenient + 
                             air.sat$Ease.of.Online.booking + 
                             air.sat$Gate.location + 
                             air.sat$Food.and.drink + 
                             air.sat$Online.boarding + 
                             air.sat$Seat.comfort + 
                             air.sat$Inflight.entertainment + 
                             air.sat$On.board.service + 
                             air.sat$Leg.room + 
                             air.sat$Baggage.handling + 
                             air.sat$Checkin.service + 
                             air.sat$Inflight.service + 
                             air.sat$Cleanliness) / 14

# create new variable of overall Average of inflight experience ratings 
air.sat$Inflight.Exp.Rating <- (air.sat$Inflight.wifi + 
                                  air.sat$Food.and.drink + 
                                  air.sat$Seat.comfort + 
                                  air.sat$Inflight.entertainment + 
                                  air.sat$On.board.service + 
                                  air.sat$Leg.room + 
                                  air.sat$Inflight.service + 
                                  air.sat$Cleanliness) / 8


# create new variable of overall Average of convience & time-saving related ratings 
air.sat$Time.Convenience.Rating <- (air.sat$Depart.Arrive.time.convenient + 
                                      air.sat$Ease.of.Online.booking + 
                                      air.sat$Gate.location + 
                                      air.sat$Online.boarding + 
                                      air.sat$Baggage.handling + 
                                      air.sat$Checkin.service) / 6


# Create numeric value (dummy variable) for Satisfaction 

air.sat$satisfaction2 <- ifelse(air.sat$satisfaction == 'satisfied', 1, 0)


########################################################  
############################ Data Exploration 
########################################################  

############################  histograms

ggplot(air.sat, aes(x=Age)) + geom_histogram(color="black", fill="white",binwidth = 1)
ggplot(air.sat, aes(x=Flight.Distance)) + geom_histogram(color="black", fill="white", binwidth = 100)
ggplot(air.sat, aes(x=Departure.Delay.in.Minutes)) + geom_histogram(color="black", fill="white", binwidth = 15)
ggplot(air.sat, aes(x=Arrival.Delay.in.Minutes)) + geom_histogram(color="black", fill="white", binwidth = 15)



############################  count / mean of variables by other categories 

air.sat %>% group_by(Purpose) %>% count(Class2)
air.sat %>% group_by(Purpose) %>% count(Gender)
air.sat %>% group_by(Purpose) %>% count(Age.Range)
air.sat %>% group_by(Class2) %>% count(Age.Range)
air.sat %>% group_by(Purpose) %>% count(satisfaction)
air.sat %>% count(Age)
air.sat %>% group_by(Purpose, Class2) %>% summarise(mean_rating = mean(Average.Rating))

counts.group <- air.sat %>% 
  group_by(Purpose, Class2, Loyalty, Gender) %>% count(Age.Range) 

counts.group2 <- air.sat %>% 
  group_by(Purpose, Class2, Loyalty, satisfaction, Gender) %>% count(Age.Range) 


avg.rate.group <- air.sat %>% 
  group_by(Purpose, Class2, Loyalty, Gender, Age.Range) %>% 
  summarise(mean_rating = mean(Average.Rating))

avg.rate.group2 <- air.sat %>% 
  group_by(satisfaction, Purpose, Class2, Loyalty, Gender, Age.Range) %>% 
  summarise(mean_rating = mean(Average.Rating))



############################ filter by Type of Travel 

air.bus <- air.sat %>%
  filter(Purpose == 'Business travel')

air.per <- air.sat %>%
  filter(Purpose == 'Personal Travel')



############################  satisfaction by type of travel 

TT <- ggplot(air.sat, aes(Purpose)) + 
  geom_bar(aes(fill = satisfaction)) +
  ggtitle('Satisfaction by Type of Travel') + theme(legend.position="none")

# satisfaction by class  

Cl <- ggplot(air.sat, aes(Class2)) + 
  geom_bar(aes(fill = satisfaction)) +
  ggtitle('Satisfaction by Cabin Class') + theme(legend.position="none")

# satisfaction by loyalty  

Cu <- ggplot(air.sat, aes(Loyalty)) + 
  geom_bar(aes(fill = satisfaction)) +
  ggtitle('Satisfaction by Customer Type') + theme(legend.position="none") 

# satisfaction by age  

AR <- ggplot(air.sat, aes(Age.Range)) + 
  geom_bar(aes(fill = satisfaction)) +
  ggtitle('Satisfaction by Age')

library(gridExtra)

grid.arrange(TT,Cl,Cu,nrow=1, ncol=3) 

grid.arrange(TT,Cl,Cu,AR, ncol = 3, nrow = 2,
             layout_matrix = rbind(c(1,2,3), c(4,4,4)))



############################  actual satisfaction average scores to satisfaction category

ggplot(air.sat, aes(x=Average.Rating)) + geom_bar(aes(fill = satisfaction)) +
  ggtitle('Satisfaction by Overall Rating Average')

s1 <- ggplot(air.per, aes(x=Average.Rating)) + geom_bar(aes(fill = satisfaction)) +
  ggtitle('Satisfaction by Overall Rating Average among Personal Travel') + 
  theme(legend.position="none") 

s2 <- ggplot(air.bus, aes(x=Average.Rating)) + geom_bar(aes(fill = satisfaction)) +
  ggtitle('Satisfaction by Overall Rating Average among Business Travel')

grid.arrange(s1, s2, nrow=1, ncol=9,
             layout_matrix = rbind(c(1,1,1,1,2,2,2,2,2)))



############################  correlations
air.num <- air.sat[, c(5,8:24,30)]
air.bus.num <- air.bus[, c(5,8:24,30)]
air.per.num <- air.per[, c(5,8:24,30)]

#library(Hmisc)

air.cor <- cor(air.num)
air.cor.bus <- cor(air.bus.num)
air.cor.per <- cor(air.per.num)

#remove variables that don't correlate to anything else
round(air.cor.bus, 2)
air.bus.num <- air.bus[, c(9:22,30)]
air.cor.bus <- cor(air.bus.num)
round(air.cor.bus, 2)

round(air.cor.per, 2)
air.per.num <- air.per[, c(5,9:11,13:22,30)]
air.cor.per <- cor(air.per.num)
round(air.cor.per, 2)



library(corrplot)
corrplot(air.cor, type = "upper", order = "hclust", tl.col = "black", tl.srt = 45)

corrplot(air.cor.bus, type = "upper", order = "hclust", tl.col = "black", tl.srt = 45)
corrplot(air.cor.per, type = "upper", order = "hclust", tl.col = "black", tl.srt = 45)


col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))

corrplot(air.cor.bus, method = "shade", shade.col = NA, tl.col = "black", tl.srt = 45,
         col = col(200), addCoef.col = "black", cl.pos = "n", order = "AOE")


corrplot(air.cor.per, method = "shade", shade.col = NA, tl.col = "black", tl.srt = 45,
         col = col(200), addCoef.col = "black", cl.pos = "n", order = "AOE")




########################################################  
############################ Pivot
########################################################  

library(tidyverse)

air.piv <- air.sat %>%
  pivot_longer(cols =  Inflight.wifi:Cleanliness,
               names_to = "Category", 
               values_to = "Rating") 


avg.rate.group.piv <- air.piv %>% 
  group_by(Purpose, Class, Loyalty, Gender, Age.Range, Category) %>% 
  summarise(mean_rating = mean(Rating))

ggplot(data=air.piv, aes(x=id, y=Rating)) +
  geom_line()





########################################################  
############################ Multidimensional Scaling   
######################################################## 

head(avg.rate.group.bus)

avg.rate.group.bus$category <- paste(avg.rate.group.bus$satisfaction,
                                     avg.rate.group.bus$Purpose,
                                     avg.rate.group.bus$Class2,
                                     avg.rate.group.bus$Loyalty,
                                     avg.rate.group.bus$Gender,
                                     avg.rate.group.bus$Age.Range)
head(avg.rate.group.bus)

avg.rate.group.bus2 <- avg.rate.group.bus[,7:21]
avg.rate.group.bus3 <- avg.rate.group.bus2
avg.rate.group.bus3$category = as.numeric(as.factor(avg.rate.group.bus3$category))

# now we scale and calculate distances and see the result
bus.dists <- avg.rate.group.bus3 %>%
  scale %>%
  dist
head(bus.dists)

# there is actually a built-in command called cmdscale
# and as you can see, the output is just the 2D coordinates
# they're in the same order as the original
mds2 <- data.frame(cmdscale(bus.dists))

# visualizing the result is just a scatterplot
ggplot(mds2, aes(X1, X2)) + 
  geom_point()

# If we want to be able to use other variables for labels or color, we will
# have to merge them back together with the projection variables.
# This is very convenient because we can just add an index column to
# each and then join on the fly using dplyr.
# At the same time, we're extracting the names of the cars from R's format
# to a real data frame column (the . means the current data frame, so it goes
# before we change everything with the first mutate).
# For more, see Tutorial 2 and Tutorial 4 (where we used join for maps).
bus.dists2 <- inner_join(avg.rate.group.bus2 %>%
                           mutate(name=rownames(.)) %>%
                           mutate(idx=1:n()),
                         mds2 %>% mutate(idx=1:n()) )

head(bus.dists2)


# now we can create charts with other mappings from the original data
ggplot(bus.dists2, aes(X1, X2)) +   
  geom_point() +
  geom_label(aes(label=category))




########################################################  
############################ Star Plot  
######################################################## 

stars(avg.rate.group.bus)

stars(avg.rate.group.bus, draw.segments=TRUE)

stars(avg.rate.group.bus[, 7:20], # subset columns
      draw.segments=TRUE, # color segments
      len = 0.8, # scale back radii a bit
      key.loc = c(12, 2), # add the key in lower right (12,2 are coordinates)
      main = "Business Travelers", # title
      full = FALSE, # can use just half the circle
      labels=abbreviate(case.names(avg.rate.group.bus))) # abbreviated labels




########################################################  
############################ Error Bars 
########################################################  

library(Rmisc) # for summarySE
# this adds standard deviation, standard error and a confidence interval
# with respect to the selected variable (len) to our data frame

air.sat$Age.Bucket <- round(air.sat$Age, -1)

tgc1 <- summarySE(air.sat, measurevar="Average.Rating", groupvars=c("Purpose","Age.Bucket"))
head(tgc1)

# Standard error of the mean
plt <- ggplot(tgc1, aes(x=Age.Bucket, y=Average.Rating, colour=Purpose))
plt +
  geom_line() +
  geom_point() +
  geom_errorbar(aes(ymin=Average.Rating-se, ymax=Average.Rating+se), width=.1)


# The errorbars overlapped, so use position_dodge to move them horizontally
pd <- position_dodge(0.1) # move them .05 to the left and right
plt + geom_errorbar(aes(ymin=Average.Rating-se, ymax=Average.Rating+se), width=.1,
                    position=pd) +
  geom_line(position=pd) +
  geom_point(position=pd)

# Use 95% confidence interval instead of SEM
# (note the change in the ymin and ymax formulas to use 'ci')
plt + 
  geom_errorbar(aes(ymin=Average.Rating-ci, ymax=Average.Rating+ci), width=.1, position=pd) +
  geom_line(position=pd) +
  geom_point(position=pd) +
  ylim(2.5,4) +
  ylab('Average Rating (scale of 0-5)') +
  xlab('Age Group') +
  ggtitle('Average Rating by Age Group')

