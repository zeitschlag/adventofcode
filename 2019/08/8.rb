require 'minitest/autorun'

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

class Layer

  attr_reader :image_data
  
  # image data = [[]]
  def initialize(image_data)
    @image_data = image_data
  end
  
  def count(number)
    @image_data.flatten.count(number)
  end
end

class LayerTests < MiniTest::Test
  def test_number_count_1
    layer = Layer.new([["7", "8", "9"], ["0", "0", "2"]])
    assert_equal 2, layer.count("0")
  end
  
  def test_number_count_2
    layer = Layer.new("222212222012220210222022222222222222222222012221222212212222012222020222212222222021222122222012102221222200022222222221202212222222222222122112222222".chars)
    assert_equal 116, layer.count("2")
  end
end

def first_puzzle
  image_data = IO.read("image_data.txt").chars
  
  layers = []
  
  for image in image_data.each_slice(IMAGE_WIDTH).each_slice(IMAGE_HEIGHT) do
    layers.append(Layer.new(image))
  end
  
  layer_with_fewest_zeros = layers.sort { |a, b| a.count("0") <=> b.count("0") }.first
  
  puts "0: #{layer_with_fewest_zeros.count("0")}, 1: #{layer_with_fewest_zeros.count("1") * layer_with_fewest_zeros.count("2")}"
end

def second_puzzle
  image_data = IO.read("image_data.txt").chars
  
  layers = []
  
  for image in image_data.each_slice(IMAGE_WIDTH).each_slice(IMAGE_HEIGHT) do
    layers.append(Layer.new(image))
  end
  
  for i in 0..IMAGE_HEIGHT do
    for j in 0..IMAGE_WIDTH do
      for layer in layers do
        if layer.image_data[i][j] != "2"
          putc layer.image_data[i][j]
          break
        end
      end
    end
    putc "\n"
  end
    
    
  # if pixel == 2: look in the next layer
  # else: return color
  
end

second_puzzle

# 0 is black
# 1 is white
# 2 is transparent
# print first visible 