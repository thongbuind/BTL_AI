import cv2

def draw_status_box(frame, detected_classes):
    BOX_CONFIG = {
        'width_ratio': 1/4,      # Tỷ lệ chiều rộng so với frame (1/4 = 25%)
        'height_ratio': 1/4,     # Tỷ lệ chiều cao so với frame
        'margin_x': 10,          # Khoảng cách từ cạnh trái
        'margin_y': 10,          # Khoảng cách từ cạnh trên
        'border_color': (200, 200, 200),  # Màu viền khung (BGR)
        'border_thickness': 4     # Độ dày viền khung
    }
    
    TITLE_CONFIG = {
        'text': 'Objects detected:',
        'offset_x': 10,          # Khoảng cách từ cạnh trái khung
        'offset_y': 25,          # Khoảng cách từ cạnh trên khung
        'font': cv2.FONT_HERSHEY_SIMPLEX,
        'font_scale': 2,         # Kích thước chữ
        'color': (255, 255, 255),  # Màu chữ (trắng)
        'thickness': 3           # Độ dày chữ
    }
    
    ITEM_CONFIG = {
        'start_y': 50,           # Vị trí bắt đầu danh sách (từ đầu khung)
        'spacing': 60,           # Khoảng cách giữa các dòng
        'offset_x': 20,          # Thụt vào từ cạnh trái khung
        'font': cv2.FONT_HERSHEY_SIMPLEX,
        'font_scale': 2,         # Kích thước chữ
        'color_detected': (0, 0, 0),      # Màu chữ khi phát hiện (đen)
        'color_undetected': (255, 255, 255),  # Màu chữ khi chưa phát hiện (trắng)
        'thickness_detected': 5,    # Độ dày chữ khi phát hiện
        'thickness_undetected': 3   # Độ dày chữ khi chưa phát hiện
    }
    
    OBJECTS = {
        "RB19": (42, 26, 106),
        "Quyt_kiem_sy": (255, 165, 0),
        "Tao_thien_xa": (50, 205, 50),
        "Thom_giac_dau": (255, 255, 0)
    }
    
    h, w, _ = frame.shape
    rect_w = int(w * BOX_CONFIG['width_ratio'])
    rect_h = int(h * BOX_CONFIG['height_ratio'])
    start_x = BOX_CONFIG['margin_x']
    start_y = BOX_CONFIG['margin_y']
    end_x = start_x + rect_w
    end_y = start_y + rect_h

    cv2.rectangle(
        frame,
        (start_x, start_y),
        (end_x, end_y),
        BOX_CONFIG['border_color'],
        BOX_CONFIG['border_thickness']
    )
    
    cv2.putText(
        frame,
        TITLE_CONFIG['text'],
        (start_x + TITLE_CONFIG['offset_x'], start_y + TITLE_CONFIG['offset_y']),
        TITLE_CONFIG['font'],
        TITLE_CONFIG['font_scale'],
        TITLE_CONFIG['color'],
        TITLE_CONFIG['thickness']
    )

    for i, (name, color) in enumerate(OBJECTS.items()):
        y = start_y + ITEM_CONFIG['start_y'] + i * ITEM_CONFIG['spacing']
        is_detected = name in detected_classes
        
        cv2.putText(
            frame,
            name.upper(),
            (start_x + ITEM_CONFIG['offset_x'], y),
            ITEM_CONFIG['font'],
            ITEM_CONFIG['font_scale'],
            ITEM_CONFIG['color_detected'] if is_detected else ITEM_CONFIG['color_undetected'],
            ITEM_CONFIG['thickness_detected'] if is_detected else ITEM_CONFIG['thickness_undetected']
        )

    return frame
