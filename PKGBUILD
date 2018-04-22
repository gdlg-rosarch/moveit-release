# Script generated with Bloom
pkgdesc="ROS - The interface for using CHOMP within MoveIt!"


pkgname='ros-lunar-moveit-planners-chomp'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-chomp-motion-planner'
'ros-lunar-cmake-modules'
'ros-lunar-moveit-core'
'ros-lunar-moveit-experimental'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
)

depends=('ros-lunar-moveit-core'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
)

conflicts=()
replaces=()

_dir=moveit_planners_chomp
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_planners_chomp $srcdir/moveit_planners_chomp
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

