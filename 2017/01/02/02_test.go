package main

import (
  "testing"
)

func TestFirstExample(t *testing.T) {
  digits := []int{1,2,1,2}
  want := 6
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}

func TestSecondExample(t *testing.T) {
  digits := []int{1,2,2,1}
  want := 0
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}

func TestThirdExample(t *testing.T) {
  digits := []int{1,2,3,4,2,5}
  want := 4
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}

func TestFourthExample(t *testing.T) {
  digits := []int{1,2,3,1,2,3}
  want := 12
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}


func TestFifthExample(t *testing.T) {
  digits := []int{1,2,1,3,1,4,1,5}
  want := 4
  have := calculateCaptcha(digits)

  if have != want {
    t.Fail()
  }
}
