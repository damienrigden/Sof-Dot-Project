# Sof-Dot-Project

Sof-Dot stands for "Switch on five, Double on ten"
This is a numbering system I invented which uses dots and dashes 
in two rows to Represent numbers in two digit increments
separated by a delimeter bar.
The file "sofdotClass" should have everything needed to use these numbers

Dots represent "ones"

    "One"       "Two"      "Three"    "Four"
    _______    _______     _______     _______  <--Delimeter Bar 
                                                <--Row 2
    ▄          ▄ ▄         ▄ ▄ ▄       ▄ ▄ ▄ ▄  <--Row 1

When you reach 5, you add a bar

    "Five"
    _______   <--Delimeter Bar 
              <--Row 2
    ▄▄▄       <--Row 1

Then continue counting up with ones on the second row

    "Six"      "Seven"    "Eight"    "Nine"
    _______    _______    _______     _______   <--Delimeter Bar
    ▄          ▄ ▄        ▄ ▄ ▄       ▄ ▄ ▄ ▄   <--Row 2
    ▄▄▄        ▄▄▄        ▄▄▄         ▄▄▄       <--Row 1

When you reach 10, the "Five Bar" doubles

    "Ten"
    _______   <--Delimeter Bar
    ▄▄▄       <--Row 2
    ▄▄▄       <--Row 1

Then continue counting up with ones on the first row

    "Eleven"   "Twelve"    "Thirteen" "Fourteen"
    _______    _______     _______     _______   <--Delimeter Bar
    ▄▄▄        ▄▄▄         ▄▄▄         ▄▄▄       <--Row 2
    ▄          ▄ ▄         ▄ ▄ ▄       ▄ ▄ ▄ ▄   <--Row 1

On 15 the "Five Bar" Changes and the cycle repeats

    "Fifteen"
    _______   <--Delimeter Bar
              <--Row 2
    ▄▄▄ ▄     <--Row 1

There is some logic behind the progression of the five bars,
but for clarity I will just list them out

    ▄▄▄     <--Five
    ▄▄▄ ▄   <--Fifteen
    ▄▄▄ ▄ ▄ <--Twenty-Five
    ▄ ▄▄▄   <--Thirty-Five
    ▄ ▄▄▄ ▄ <--Forty-Five
    ▄ ▄ ▄▄▄ <--Fifty-Five
    ▄▄▄▄▄   <--Sixty-Five
    ▄▄▄▄▄ ▄ <--Seventy-Five
    ▄ ▄▄▄▄▄ <--Eighty-Five
    ▄▄▄ ▄▄▄ <--Ninety-Five

Numbers Longer Than Two Digits Are represented by successive rows
Reading from bottom to top

    "6732"
    _______
    ▄▄▄ ▄ ▄
    ▄ ▄
    _______
    ▄ ▄
    ▄▄▄▄▄

Thanks for reading, and welcome to this repository!
