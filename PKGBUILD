# Script generated with Bloom
pkgdesc="ROS - Components of MoveIt connecting to perception"
url='http://moveit.ros.org'

pkgname='ros-lunar-moveit-ros-perception'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'freeglut'
'glew'
'mesa'
'ros-lunar-catkin'
'ros-lunar-cv-bridge'
'ros-lunar-image-transport'
'ros-lunar-message-filters'
'ros-lunar-moveit-core'
'ros-lunar-moveit-msgs'
'ros-lunar-octomap'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-tf'
'ros-lunar-tf-conversions'
'ros-lunar-urdf'
)

depends=('freeglut'
'glew'
'mesa'
'ros-lunar-cv-bridge'
'ros-lunar-image-transport'
'ros-lunar-message-filters'
'ros-lunar-moveit-core'
'ros-lunar-moveit-msgs'
'ros-lunar-octomap'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-tf'
'ros-lunar-tf-conversions'
'ros-lunar-urdf'
)

conflicts=()
replaces=()

_dir=moveit_ros_perception
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_ros_perception $srcdir/moveit_ros_perception
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

