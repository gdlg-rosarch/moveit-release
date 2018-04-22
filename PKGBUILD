# Script generated with Bloom
pkgdesc="ROS - Components of MoveIt that offer interaction via interactive markers"
url='http://moveit.ros.org'

pkgname='ros-kinetic-moveit-ros-robot-interaction'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-eigen-conversions'
'ros-kinetic-interactive-markers'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-pluginlib>=1.10.4'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
)

depends=('ros-kinetic-eigen-conversions'
'ros-kinetic-interactive-markers'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-pluginlib>=1.10.4'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=moveit_ros_robot_interaction
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_ros_robot_interaction $srcdir/moveit_ros_robot_interaction
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

