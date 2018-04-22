# Script generated with Bloom
pkgdesc="ROS - Components of MoveIt that offer simpler interfaces to planning and execution"
url='http://moveit.ros.org'

pkgname='ros-lunar-moveit-ros-planning-interface'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'python2'
'python2-catkin_pkg'
'ros-lunar-actionlib'
'ros-lunar-catkin'
'ros-lunar-eigen-conversions'
'ros-lunar-moveit-resources'
'ros-lunar-moveit-ros-manipulation'
'ros-lunar-moveit-ros-move-group'
'ros-lunar-moveit-ros-planning'
'ros-lunar-moveit-ros-warehouse'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-rostest'
'ros-lunar-tf'
'ros-lunar-tf-conversions'
)

depends=('python2'
'ros-lunar-actionlib'
'ros-lunar-eigen-conversions'
'ros-lunar-moveit-ros-manipulation'
'ros-lunar-moveit-ros-move-group'
'ros-lunar-moveit-ros-planning'
'ros-lunar-moveit-ros-warehouse'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-tf'
'ros-lunar-tf-conversions'
)

conflicts=()
replaces=()

_dir=moveit_ros_planning_interface
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_ros_planning_interface $srcdir/moveit_ros_planning_interface
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

