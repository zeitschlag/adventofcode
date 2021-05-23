package main

import (
  "testing"
)

func TestFirstExample(t *testing.T) {
  digits := []int{1,1,2,2}
  want := 3
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}

func TestSecondExample(t *testing.T) {
  digits := []int{1,1,1,1}
  want := 4
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}

func TestThirdExample(t *testing.T) {
  digits := []int{1,2,3,4}
  want := 0
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}

func TestFourthExample(t *testing.T) {
  digits := []int{9,1,2,1,2,1,2,9}
  want := 9
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}
