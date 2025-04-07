---
title: "Cereal and Toyota Analysis"
author: "Your Name"
output: html_document
---

# 4.2 Cereal Dataset

### 평균

```{r mean_values}
cereals.df<-read.csv("D:/Desktop/to/Cereals.csv")
cereals.df
```

```{r mean_values}
cereal_numeric<-cereals.df[,sapply(cereals.df,is.numeric)]
```

```{r mean_values}
sapply(cereal_numeric,mean,na.rm=TRUE)
```

```{r mean_values}
sapply(cereal_numeric,min,na.rm=TRUE)
```
