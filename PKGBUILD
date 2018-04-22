# Script generated with Bloom
pkgdesc="ROS - Components of MoveIt that offer visualization"
url='http://moveit.ros.org'

pkgname='ros-kinetic-moveit-ros-visualization'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'pkg-config'
'ros-kinetic-catkin'
'ros-kinetic-geometric-shapes'
'ros-kinetic-interactive-markers'
'ros-kinetic-moveit-ros-perception'
'ros-kinetic-moveit-ros-planning-interface'
'ros-kinetic-moveit-ros-robot-interaction'
'ros-kinetic-moveit-ros-warehouse'
'ros-kinetic-object-recognition-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-rostest'
'ros-kinetic-rviz'
)

depends=('ros-kinetic-geometric-shapes'
'ros-kinetic-interactive-markers'
'ros-kinetic-moveit-ros-perception'
'ros-kinetic-moveit-ros-planning-interface'
'ros-kinetic-moveit-ros-robot-interaction'
'ros-kinetic-moveit-ros-warehouse'
'ros-kinetic-object-recognition-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-rviz'
)

conflicts=()
replaces=()

_dir=moveit_ros_visualization
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_ros_visualization $srcdir/moveit_ros_visualization
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

