class ClassPlayer:
    def __init__(self, player_id, name_player, speed_score, technique_score, goal_score):
        self.id = player_id
        self.name_player = name_player
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score
        self.calculate_average = 0.0
        self.inventory_type = ""
        self.calculate_inventory_value()
        self.classify_performance()

    def calculate_inventory_value(self):
        self.calculate_average = (self.speed_score * 0.3) + (self.technique_score * 0.4) + (self.goal_score * 0.4)

    def classify_performance(self):
        if self.calculate_average < 5:
            self.inventory_type = "Dự bị yếu"
        elif self.calculate_average < 6.5:
            self.inventory_type = "Trung bình"
        elif self.calculate_average < 8:
            self.inventory_type = "Tốt"
        else:
            self.inventory_type = "Ngôi sao"

class PlayerManager:
    def __init__(self):
        self.players = []

    def is_id_exist(self, player_id):
        for player in self.players:
            if str(player.id).strip().lower() == str(player_id).strip().lower():
                return True
        return False

    def show_all(self):
        if not self.players:
            print("\nDanh sách cầu thủ đang rỗng!")
            return
        print("\n" + "="*75)
        print(f"{'Mã cầu thủ':<12} | {'Họ tên':<20} | {'Điểm tốc độ':<12} | {'Điểm kỹ thuật':<15} | {'Điểm ghi bàn':<12}")
        print("="*75)
        for o in self.players:
            print(f"{o.id:<12} | {o.name_player:<20} | {o.speed_score:<12.1f} | {o.technique_score:<15.1f} | {o.goal_score:<12.1f}")
        print("="*75)

    def add_player(self, obj):
        self.players.append(obj)
        print("\nThêm cầu thủ thành công!")

    def update_player(self, player_id, new_speed, new_technique, new_goal):
        for player in self.players:
            if str(player.id).strip().lower() == str(player_id).strip().lower():
                player.speed_score = new_speed
                player.technique_score = new_technique
                player.goal_score = new_goal
                player.calculate_inventory_value()
                player.classify_performance()
                print("\nCập nhật cầu thủ thành công!")
                return True
        return False

    def delete_player(self, player_id):
        for i, player in enumerate(self.players):
            if str(player.id).strip().lower() == str(player_id).strip().lower():
                confirm = input("Bạn có chắc muốn xóa cầu thủ này không? (Y/N): ").strip().lower()
                if confirm == 'y':
                    self.players.pop(i)
                    print("\nXóa cầu thủ thành công!")
                elif confirm == 'n':
                    print("\nHủy bỏ thao tác xóa.")
                else:
                    print("\nNhập chưa đúng")
                return True
        return False

    def search_player(self, keyword):
        keyword = keyword.strip().lower()
        results = []
        for player in self.players:
            if keyword in player.name_player.lower() or keyword in player.inventory_type.lower():
                results.append(player)
        if not results:
            print("\nKhông tìm thấy cầu thủ phù hợp!")
            return
        print(f"\nĐã tìm thấy {len(results)} kết quả phù hợp:")
        temp_PlayerManager = PlayerManager()
        temp_PlayerManager.players = results
        temp_PlayerManager.show_all()

def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value: 
            return value
        print("Không được để trống!")

def get_valid_number(prompt, is_int=False, min_val=0, max_val=None):
    while True:
        try:
            user_input = input(prompt).strip()
            value = int(user_input) if is_int else float(user_input)
            if min_val is not None and value < min_val:
                print(f"Giá trị phải lớn hơn hoặc bằng {min_val}!")
                continue
            if max_val is not None and value > max_val:
                print(f"Giá trị không được vượt quá {max_val:,}!")
                continue
            return value
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

def main():
    manager = PlayerManager()
    while True:
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách cầu thủ")
        print("2. Thêm cầu thủ mới")
        print("3. Cập nhật cầu thủ")
        print("4. Xóa cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("6. Thoát")
        print("=====================================")
        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case '1':
                manager.show_all()
            case '2':
                print("\nThêm cầu thủ")
                while True:
                    player_id = get_non_empty_string("Nhập mã cầu thủ: ")
                    if manager.is_id_exist(player_id):
                        print("Mã cầu thủ đã tồn tại!")
                    else:
                        break
                name_player = get_non_empty_string("Nhập họ tên cầu thủ: ")
                speed_score = get_valid_number("Nhập điểm tốc độ: ", is_int=False, min_val=0, max_val=10)
                technique_score = get_valid_number("Nhập điểm kỹ thuật: ", is_int=False, min_val=0, max_val=10)
                goal_score = get_valid_number("Nhập điểm ghi bàn: ", is_int=False, min_val=0, max_val=10)
                new_player = ClassPlayer(player_id, name_player, speed_score, technique_score, goal_score)
                manager.add_player(new_player)
            case '3':
                print("\nCập nhật cầu thủ")
                player_id = input("Nhập mã cầu thủ cần cập nhật: ").strip()
                if not manager.is_id_exist(player_id):
                    print("Không tìm thấy cầu thủ cần cập nhật!")
                else:
                    new_speed = get_valid_number("Nhập điểm tốc độ mới: ", is_int=False, min_val=0, max_val=10)
                    new_technique = get_valid_number("Nhập điểm kỹ thuật mới: ", is_int=False, min_val=0, max_val=10)
                    new_goal = get_valid_number("Nhập điểm ghi bàn mới: ", is_int=False, min_val=0, max_val=10)
                    manager.update_player(player_id, new_speed, new_technique, new_goal)
            case '4':
                print("\nXóa cầu thủ")
                player_id = input("Nhập mã cầu thủ cần xóa: ").strip()
                if not manager.delete_player(player_id):
                    print("Không tìm thấy cầu thủ cần xóa!")
            case '5':
                print("\nTìm kiếm cầu thủ")
                keyword = input("Nhập tên hoặc danh mục/loại cầu thủ cần tìm: ")
                manager.search_player(keyword)
            case '6':
                print("\nCảm ơn bạn đã sử dụng hệ thống quản lý cầu thủ bóng đá!")
                break
            case _:
                print("\nVui lòng nhập số từ 1 đến 6.")

if __name__ == "__main__":
    main()