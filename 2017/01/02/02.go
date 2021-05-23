package main

import (
  "fmt"
  "io/ioutil"
)

func readList(filename string) ([]int, error) {
  data, err := ioutil.ReadFile(filename)

  if err != nil {
    return nil, err
  }

  filecontent := string(data)

  var digits []int

  for _, strDigit := range filecontent {
    // these seems to be the dirty way to convert a rune to an int
    // https://stackoverflow.com/a/21322694
    digit := int(strDigit - '0')
    digits = append(digits, digit)
  }

  return digits, nil
}

func calculateCaptcha(digits []int) int {

  delta := len(digits)/2
  doubleDigits := digits
  for _, elem := range digits {
    doubleDigits = append(doubleDigits,elem)
  }

  var captcha int
  // iterate over all those digits
  for index, digit := range digits {
    // compare with the one half in 0.5 len
    if digit == doubleDigits[index+delta] {
      // if they match: add the value to captcha
      captcha = captcha + digit
    }
  }

  return captcha
}

func main() {
  digits, _ := readList("input.txt")
  captcha := calculateCaptcha(digits)
  fmt.Println(captcha)
}
