li_ = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([li_[i + 1] for i in range(len(li_) - 1) if li_[i] < li_[i + 1]])