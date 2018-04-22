# Script generated with Bloom
pkgdesc="ROS - Core libraries used by MoveIt!"
url='http://moveit.ros.org'

pkgname='ros-kinetic-moveit-core'
pkgver='0.9.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('assimp'
'boost'
'console-bridge'
'eigen3'
'fcl'
'pkg-config'
'ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-eigen-conversions'
'ros-kinetic-eigen-stl-containers'
'ros-kinetic-geometric-shapes>=0.5.2'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-parser'
'ros-kinetic-moveit-msgs'
'ros-kinetic-moveit-resources'
'ros-kinetic-octomap'
'ros-kinetic-octomap-msgs'
'ros-kinetic-orocos-kdl'
'ros-kinetic-random-numbers'
'ros-kinetic-roslib'
'ros-kinetic-rostime'
'ros-kinetic-rosunit'
'ros-kinetic-sensor-msgs'
'ros-kinetic-shape-msgs'
'ros-kinetic-srdfdom'
'ros-kinetic-std-msgs'
'ros-kinetic-tf-conversions'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'urdfdom'
'urdfdom-headers'
)

depends=('assimp'
'boost'
'console-bridge'
'eigen3'
'fcl'
'ros-kinetic-eigen-conversions'
'ros-kinetic-eigen-stl-containers'
'ros-kinetic-geometric-shapes>=0.5.2'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-parser'
'ros-kinetic-moveit-msgs'
'ros-kinetic-octomap'
'ros-kinetic-octomap-msgs'
'ros-kinetic-random-numbers'
'ros-kinetic-rostime'
'ros-kinetic-sensor-msgs'
'ros-kinetic-srdfdom'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'urdfdom'
'urdfdom-headers'
)

conflicts=()
replaces=()

_dir=moveit_core
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_core $srcdir/moveit_core
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

