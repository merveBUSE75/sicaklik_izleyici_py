cd ~/ros2_ws/src/sicaklik_izleyici_py

cat << 'EOF' > README.md
# Sıcaklık İzleyici (ROS 2)

Bu paket, rastgele sıcaklık verisi üreten bir sensör düğümü ile bu veriyi dinleyip belirlenen eşik değerini aştığında uyarı veren bir izleyici düğümünden oluşur.

## Gereksinimler
- ROS 2 (rclpy, std_msgs)

## Kurulum ve Derleme
Çalışma alanının ana dizininde paketi derleyin ve ortam değişkenlerini yükleyin:

```bash
cd ~/ros2_ws
colcon build --packages-select sicaklik_izleyici_py
source install/setup.bash
