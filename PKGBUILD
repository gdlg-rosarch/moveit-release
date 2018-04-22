# Script generated with Bloom
pkgdesc="ROS - ros_control controller manager interface for MoveIt!"


pkgname='ros-lunar-moveit-ros-control-interface'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-catkin'
'ros-lunar-controller-manager-msgs'
'ros-lunar-moveit-core'
'ros-lunar-moveit-simple-controller-manager'
'ros-lunar-pluginlib>=1.10.4'
'ros-lunar-trajectory-msgs'
)

depends=('ros-lunar-actionlib'
'ros-lunar-controller-manager-msgs'
'ros-lunar-moveit-core'
'ros-lunar-moveit-simple-controller-manager'
'ros-lunar-pluginlib>=1.10.4'
'ros-lunar-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=moveit_ros_control_interface
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_ros_control_interface $srcdir/moveit_ros_control_interface
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

