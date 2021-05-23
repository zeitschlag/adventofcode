package main

import (
  "fmt"
  "io/ioutil"
//  "errors"
)

func readList(filename string) ([]int, error) {
  data, err := ioutil.ReadFile(filename)

  if err != nil {
    return nil, err
  }

  // I have some kind of data
  // I have to make an int-slice out of this data

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
  var captcha int
  // iterate over all those digits
  // compare with next one
  // if they match: add the value to captcha
  // if you reach the end, compare with first one
  for index, digit := range digits {
    if index == len(digits)-1 {
      if digit == digits[0] {
        captcha = captcha + digit
      }
      return captcha
    }

    if digit == digits[index+1] {
      captcha = captcha + digit
    }
  }

  return captcha
}

func main() {
  digits, _ := readList("input.txt")
  fmt.Println(digits)
  captcha := calculateCaptcha(digits)
  fmt.Println(captcha)
}
