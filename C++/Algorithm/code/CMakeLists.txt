cmake_minimum_required(VERSION 3.20)
project(Algorithm)

set(CMAKE_CXX_STANDARD 11)
include_directories(./utils.h)

add_executable(binary_search binary_search.cpp)