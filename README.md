![Royal Road](img/rrlogo.jpg)

---

***Welcome weary traveler. You have now taken your first step into the beyond, welcome to the royal road!***

<details>

 <summary>What is Royal Road?</summary>

 > [Royal Road®](https://www.royalroad.com/home) is the home of web novels and fan fiction! In their amazing community, you can find various talented individuals who write as a hobby or even professionally, artists who create art for them, and many, many readers who provide valuable feedback and encouragement.

</details>
<br />

**Overview**

This project aims to determine the rating of a novel based on its content, i.e., first five chapters, novel summary, and novel genre tags. The goal is to generate a user rating for [Royal Road's ongoing fiction novels](https://www.royalroad.com/fictions/active-popular). Essentially we are trying to answer the following question:

<div align="center"> <b> Can an algorithm rate a novel? </b> </div>

**Data**

<details>

<summary> All data was acquired from Royal Road's ongoing fiction novel pages on March 29, 2021. The following was collected:
</summary>

Total Collected :|2719|  |       |
:---------:|:-------:|:---------:|:------------:|
Titles| Genres|Followers|Number of Pages|
Number of Chapters|Chapter 1 | Chapter 2| Chapter 3|
Chapter 4 | Chapter 5| Date Last Updated| Number of Views|
Rating |

</details display="none">
<br />

*Refrence [Slides Show](pp/Presentation.pptx) for EDA and Perprocessing steps*

**Machine Learning Models**

<div align="center">
<details open>
<summary><i>Random Forest Regressor</i></summary>

R-Squared: **51%**

<div align="left">

> R-squared explains how well the model is at being accurate. A score of 100% means that it is never wrong. Our score of 51% means that half of all novel ratings predicted by the model is accurate.
</div>

</details>

</div>

<div align="center">
<details open>
<summary><i>Random Forest Classifier</i></summary>

F1-Score: **79%**

<div align="left">

> F1-Score computes accuracy of binary outcomes i.e. (Good or Bad). In this case the novel rating is divided into two groups, greater than 4 stars or less. We are simply trying to rate novels as good or bad. A F1-Score of 100% means that the model is never wrong. Our score of 79% means that the model can almost always determine weather a book is good.

</div>
</details>
</div>

**Conclusion**

It is possible for an algorithm to rate a novel simply by its' content. Specifcally for Royal Road the key genres that are highly rated are: LitRPG and Transformation.

---
