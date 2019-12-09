require 'minitest/autorun'

class Layer
  
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

image_data = IO.read("image_data.txt").chars
image_width = 25
image_height = 6

layers = []

for image in image_data.each_slice(image_width).each_slice(image_height) do
  layers.append(Layer.new(image))
end

layer_with_fewest_zeros = layers.sort { |a, b| a.count("0") <=> b.count("0") }.first

puts "0: #{layer_with_fewest_zeros.count("0")}, 1: #{layer_with_fewest_zeros.count("1") * layer_with_fewest_zeros.count("2")}"


