# Script generated with Bloom
pkgdesc="ROS - Generates a configuration package that makes it easy to use MoveIt!"
url='http://moveit.ros.org'

pkgname='ros-lunar-moveit-setup-assistant'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-moveit-core'
'ros-lunar-moveit-ros-planning'
'ros-lunar-moveit-ros-visualization'
'ros-lunar-srdfdom>0.3.1'
'yaml-cpp'
)

depends=('ros-lunar-moveit-core'
'ros-lunar-moveit-ros-planning'
'ros-lunar-moveit-ros-visualization'
'ros-lunar-srdfdom>0.3.1'
'ros-lunar-xacro'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=moveit_setup_assistant
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_setup_assistant $srcdir/moveit_setup_assistant
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

