class ColorAuth:
    def __init__(self):
        self.monday_color = {}
        self.tuesday_color = {}
        self.wednesday_color = {}
        self.thursday_color = {}
        self.friday_color = {}

        self.all_color_dict = {}

        self.counter = 0

        self.colors = []

    def set_colors(self, file, color_id):
        """RECEIVES FILES, KEEP COUNT OF THE FILES AND EXTRACT THE TEXT IN IT"""
        """GETS THE COLOR TO EFFECT WITH THE PROVIDED ID"""
        with open(file, "r") as f:
            file_content = f.readlines()
            file_content = [text.replace("\n", "") for text in file_content]
            if color_id == 1:
                for i in range(len(file_content)):
                    if file_content[i] in self.monday_color.keys():
                        self.monday_color[file_content[i]] += 1
                    else:
                        self.monday_color[file_content[i]] = 1

                # Adding to the all color dict
                self.all_color_dict.update(self.monday_color)

                # ADD THE COLORS IN EXISTENCE
                self.colors += self.get_day_color_mean(self.monday_color)

            elif color_id == 2:
                for i in range(len(file_content)):
                    if file_content[i] in self.tuesday_color.keys():
                        self.tuesday_color[file_content[i]] += 1
                    else:
                        self.tuesday_color[file_content[i]] = 1
                # Adding to the all color dict
                self.all_color_dict.update(self.tuesday_color)

                # ADD THE COLORS IN EXISTENCE
                self.colors += self.get_day_color_mean(self.tuesday_color)

            elif color_id == 3:
                for i in range(len(file_content)):
                    if file_content[i] in self.wednesday_color.keys():
                        self.wednesday_color[file_content[i]] += 1
                    else:
                        self.wednesday_color[file_content[i]] = 1
                # Adding to the all color dict
                self.all_color_dict.update(self.wednesday_color)

                # ADD THE COLORS IN EXISTENCE
                self.colors += self.get_day_color_mean(self.wednesday_color)

            elif color_id == 4:
                for i in range(len(file_content)):
                    if file_content[i] in self.thursday_color.keys():
                        self.thursday_color[file_content[i]] += 1
                    else:
                        self.thursday_color[file_content[i]] = 1

                # Adding to the all color dict
                self.all_color_dict.update(self.friday_color)

                # Adding to the all color dict
                self.all_color_dict.update(self.wednesday_color)

                # ADD THE COLORS IN EXISTENCE
                self.colors += self.get_day_color_mean(self.thursday_color)

            else:
                for i in range(len(file_content)):
                    if file_content[i] in self.friday_color.keys():
                        self.friday_color[file_content[i]] += 1
                    else:
                        self.friday_color[file_content[i]] = 1
                # Adding to the all color dict
                self.all_color_dict.update(self.thursday_color)

                # ADD THE COLORS IN EXISTENCE
                self.colors += self.get_day_color_mean(self.friday_color)

    def get_day_color_mean(self, kwargs):
        """GETS THE MEAN OF THE COLOR FOR EACH WORKING DAY"""
        value_list = []
        for key, value in kwargs.items():
            for count in range(value):
                self.counter += 1
                # ADDING THE COLOR THE NUMBER OF TIMES IT OCCURS
                value_list.append(key)
        return value_list

    def print_mean_color(self):
        index = int(len(self.colors)/self.counter)
        print(f"The mean color is: {self.colors[index]}")

    def print_most_worn_color(self):
        most_color = max(self.all_color_dict, key=self.all_color_dict.get)
        print(f"Color that's mostly worn is {most_color}")

    def print_median(self):
        median_color = self.colors[int(len(self.colors)/2)]
        print(f"The median color is {median_color}")

    def print_variance(self):
        total_color = len(self.colors)
        total_color_frequency = sum(self.all_color_dict.values())
        color_mean = total_color_frequency/total_color
        variance = pow((total_color - color_mean), 2)/total_color_frequency

        print(f"The variance of the color is: {variance}")

    def print_prop_red(self):
        total_red_color = self.all_color_dict["RED"]
        total_color = sum(self.all_color_dict.values())

        print(f"The probability of picking red is {total_red_color/total_color}")


color_auth = ColorAuth()
file_list = ["monday.txt", "tuesday.txt", "wednesday.txt", "thursday.txt", "friday.txt"]
for i in range(len(file_list)):
    color_auth.set_colors(str(file_list[i]), i)

# PRINTING THE MEAN COLOR
color_auth.print_mean_color()

# PRINT MOST WORN COLOR
color_auth.print_most_worn_color()

# PRINT THE MEDAIN COLOR
color_auth.print_mean_color()

# PRINT THE VARIANCE
color_auth.print_variance()

# PRINTE PROBABILITY OF PICKING RED
color_auth.print_prop_red()
