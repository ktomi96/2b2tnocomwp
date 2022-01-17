#!/usr/bin/python
# {
# "id": "wp1",
#  "name": "-190, 45",
#  "icon": "waypoint-normal.png",
#  "x": -190,
#  "y": 63,
#  "z": 0,
#  "r": 0,
#  "g": 203,
#  "b": 0,
#  "enable": true,
#  "type": "Normal",
#  "origin": "journeymap",
#  "dimensions": [
#   0
#  ],
#  "persistent": true
# }
#

def get_journay_waypoint_dir():
    with open("config.txt", "r", encoding="utf-8") as pth:
        path = pth.readline().strip()
        return path


def render_waypoint_file_content(cord, name, color):
    return (f'{{"id": "{cord[0]} {cord[1]}", '
            f'"name": "{name}", "icon": "waypoint-normal.png", '
            f'"x": {cord[0]}, "y": 45, "z": {cord[1]}, '
            f'"r": {color[0]}, "g": {color[1]}, "b": {color[2]}, '
            f'"enable": false, "type": "Normal", "origin": "journeymap", '
            f' "dimensions": [0], "persistent": true }}')


def get_color(counter):
    colors = [
        (255, 0, 0),
        (255, 128, 0),
        (255, 255, 0),
        (128, 255, 0),
        (0, 255, 0),
        (0, 255, 128),
        (0, 255, 255),
        (0, 128, 255),
        (0, 0, 255),
        (127, 0, 255),
        (255, 0, 255),
        (255, 0, 127)
    ]
    return colors[counter % len(colors)]


def generate_waypoint_name(_cord, counter):
    return f"wp_{counter}"


def create_file_with_content(file_path, content):
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(content)


def main(waypoints_file_path):
    coords = []
    with open(waypoints_file_path, "r", encoding='utf-8') as waypoints_file:
        for line in waypoints_file:
            coord = line.split()
            coords.append(coord)

    sorted(coords)

    counter = 0
    for coord in coords:
        path = get_journay_waypoint_dir()
        name = generate_waypoint_name(coord, counter)

        color = get_color(counter)
        waypoint_json = render_waypoint_file_content(coord, name, color)
        create_file_with_content(f"{path}/{name}.json", waypoint_json)

        counter += 1

    print(f"{counter} waypoint generated")


if __name__ == '__main__':
    main("waypoints.txt")
