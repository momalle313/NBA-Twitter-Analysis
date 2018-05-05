## CSE 40437
## NBA Game Predictor
## Sentiment Analysis

## Setup
this.dir = dirname(rstudioapi::getActiveDocumentContext()$path)
setwd(this.dir)
data_all=read.csv('Social_Sensing_NBA_Data.csv',header=T)


## Models for all 3 teams together
detach(data)
data=data_all
data
attach(data)
mod1=glm(Result..1.0.~Average.Sentiment,family=binomial,data=data)
summary(mod1)
mod2=glm(Result..1.0.~Average.Sentiment+N,family=binomial,data=data)
summary(mod2)
mod6=glm(Result..1.0.~N,family=binomial,data=data)
summary(mod6)
c(data$Result..1.0.,fitted(mod1))
data2=data.frame(data$Result..1.0.)
data2$fitted=fitted(mod1)
data2


## ROC Curve for all 3 teams together
cor(Average.Sentiment,Result..1.0.)
n=dim(data)[1]
pi0<-seq(from=0,to=1,by=0.01)
sens.vec<-NULL
spec.vec<-NULL
for (p in 1:length(pi0)){
  class.p<-rep(0,n)
  class.p[which(mod1$fitted.values>pi0[p])]<-1
  sens.p<-length(which(class.p==1 & Result..1.0.==1))/length(which(Result..1.0.==1))
  spec.p<-length(which(class.p==0 & Result..1.0.==0))/length(which(Result..1.0.==0))
  sens.vec<-c(sens.vec,sens.p)
  spec.vec<-c(spec.vec,spec.p)
}
plot(1-spec.vec,sens.vec,ylim=c(0,1),xlim=c(0,1))
pi0[which.max(spec.vec+sens.vec)]
points((1-spec.vec)[which.max(spec.vec+sens.vec)],sens.vec[which.max(spec.vec+sens.vec)],col=2,pch=16)
# Optimal probability threshold is ~0.53.
library(pROC)
roc(data$Result..1.0., data$Average.Sentiment) 
# AUC is 0.697, which is on scale fom [0.5,1.0], so it is not ideal, but still decent
roc1 <- roc(data$Result..1.0.,
            data$Average.Sentiment, percent=TRUE,
            # arguments for ci
            ci=TRUE, boot.n=100, ci.alpha=0.9, stratified=FALSE,
            # arguments for plot
            plot=TRUE, auc.polygon=TRUE, max.auc.polygon=TRUE, grid=TRUE,
            print.auc=TRUE, show.thres=TRUE)
ci(roc1)


## Model and ROC Curve for Bulls
detach(data)
data=data_all[data_all$Team=="Bulls",]
data
attach(data)
cor(Average.Sentiment,Result..1.0.)
mod3=glm(Result..1.0.~Average.Sentiment,family=binomial,data=data)
summary(mod3)
n=dim(data)[1]
pi0<-seq(from=0,to=1,by=0.01)
sens.vec<-NULL
spec.vec<-NULL
for (p in 1:length(pi0)){
  class.p<-rep(0,n)
  class.p[which(mod1$fitted.values>pi0[p])]<-1
  sens.p<-length(which(class.p==1 & Result..1.0.==1))/length(which(Result..1.0.==1))
  spec.p<-length(which(class.p==0 & Result..1.0.==0))/length(which(Result..1.0.==0))
  sens.vec<-c(sens.vec,sens.p)
  spec.vec<-c(spec.vec,spec.p)
}
plot(1-spec.vec,sens.vec,ylim=c(0,1),xlim=c(0,1))
pi0[which.max(spec.vec+sens.vec)]
points((1-spec.vec)[which.max(spec.vec+sens.vec)],sens.vec[which.max(spec.vec+sens.vec)],col=2,pch=16)
# Optimal probability threshold is ~0.41.
library(pROC)
roc(data$Result..1.0., data$Average.Sentiment) 
# AUC is 0.7143, which is on scale fom [0.5,1.0], so it is not ideal, but still decent
roc1 <- roc(data$Result..1.0.,
            data$Average.Sentiment, percent=TRUE,
            # arguments for ci
            ci=TRUE, boot.n=100, ci.alpha=0.9, stratified=FALSE,
            # arguments for plot
            plot=TRUE, auc.polygon=TRUE, max.auc.polygon=TRUE, grid=TRUE,
            print.auc=TRUE, show.thres=TRUE)
ci(roc1)


## Model and ROC Curve for Heat
detach(data)
data=data_all[data_all$Team=="Heat",]
data
attach(data)
cor(Average.Sentiment,Result..1.0.)
mod4=glm(Result..1.0.~Average.Sentiment,family=binomial,data=data)
summary(mod4)
n=dim(data)[1]
pi0<-seq(from=0,to=1,by=0.01)
sens.vec<-NULL
spec.vec<-NULL
for (p in 1:length(pi0)){
  class.p<-rep(0,n)
  class.p[which(mod1$fitted.values>pi0[p])]<-1
  sens.p<-length(which(class.p==1 & Result..1.0.==1))/length(which(Result..1.0.==1))
  spec.p<-length(which(class.p==0 & Result..1.0.==0))/length(which(Result..1.0.==0))
  sens.vec<-c(sens.vec,sens.p)
  spec.vec<-c(spec.vec,spec.p)
}
plot(1-spec.vec,sens.vec,ylim=c(0,1),xlim=c(0,1))
pi0[which.max(spec.vec+sens.vec)]
points((1-spec.vec)[which.max(spec.vec+sens.vec)],sens.vec[which.max(spec.vec+sens.vec)],col=2,pch=16)
# Optimal probability threshold is ~0.
library(pROC)
roc(data$Result..1.0., data$Average.Sentiment) 
# AUC is 0.5, which is on scale fom [0.5,1.0], so it is the worst possible.
roc1 <- roc(data$Result..1.0.,
            data$Average.Sentiment, percent=TRUE,
            # arguments for ci
            ci=TRUE, boot.n=100, ci.alpha=0.9, stratified=FALSE,
            # arguments for plot
            plot=TRUE, auc.polygon=TRUE, max.auc.polygon=TRUE, grid=TRUE,
            print.auc=TRUE, show.thres=TRUE)
ci(roc1)


## Model and ROC Curve for Rockets
detach(data)
data=data_all[data_all$Team=="Rockets",]
data
attach(data)
cor(Average.Sentiment,Result..1.0.)
mod5=glm(Result..1.0.~Average.Sentiment,family=binomial,data=data)
summary(mod5)
n=dim(data)[1]
pi0<-seq(from=0,to=1,by=0.01)
sens.vec<-NULL
spec.vec<-NULL
for (p in 1:length(pi0)){
  class.p<-rep(0,n)
  class.p[which(mod1$fitted.values>pi0[p])]<-1
  sens.p<-length(which(class.p==1 & Result..1.0.==1))/length(which(Result..1.0.==1))
  spec.p<-length(which(class.p==0 & Result..1.0.==0))/length(which(Result..1.0.==0))
  sens.vec<-c(sens.vec,sens.p)
  spec.vec<-c(spec.vec,spec.p)
}
plot(1-spec.vec,sens.vec,ylim=c(0,1),xlim=c(0,1))
pi0[which.max(spec.vec+sens.vec)]
points((1-spec.vec)[which.max(spec.vec+sens.vec)],sens.vec[which.max(spec.vec+sens.vec)],col=2,pch=16)
# Optimal probability threshold is ~0.
library(pROC)
roc(data$Result..1.0., data$Average.Sentiment) 
# AUC is 0.6429, which is on scale fom [0.5,1.0], so it is not great
roc1 <- roc(data$Result..1.0.,
            data$Average.Sentiment, percent=TRUE,
            # arguments for ci
            ci=TRUE, boot.n=100, ci.alpha=0.9, stratified=FALSE,
            # arguments for plot
            plot=TRUE, auc.polygon=TRUE, max.auc.polygon=TRUE, grid=TRUE,
            print.auc=TRUE, show.thres=TRUE)
ci(roc1)
