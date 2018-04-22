# Script generated with Bloom
pkgdesc="ROS - Core libraries used by MoveIt!"
url='http://moveit.ros.org'

pkgname='ros-lunar-moveit-core'
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
'ros-lunar-angles'
'ros-lunar-catkin'
'ros-lunar-eigen-conversions'
'ros-lunar-eigen-stl-containers'
'ros-lunar-geometric-shapes>=0.5.2'
'ros-lunar-geometry-msgs'
'ros-lunar-kdl-parser'
'ros-lunar-moveit-msgs'
'ros-lunar-moveit-resources'
'ros-lunar-octomap'
'ros-lunar-octomap-msgs'
'ros-lunar-orocos-kdl'
'ros-lunar-random-numbers'
'ros-lunar-roslib'
'ros-lunar-rostime'
'ros-lunar-rosunit'
'ros-lunar-sensor-msgs'
'ros-lunar-shape-msgs'
'ros-lunar-srdfdom'
'ros-lunar-std-msgs'
'ros-lunar-tf-conversions'
'ros-lunar-trajectory-msgs'
'ros-lunar-urdf'
'ros-lunar-visualization-msgs'
'urdfdom'
'urdfdom-headers'
)

depends=('assimp'
'boost'
'console-bridge'
'eigen3'
'fcl'
'ros-lunar-eigen-conversions'
'ros-lunar-eigen-stl-containers'
'ros-lunar-geometric-shapes>=0.5.2'
'ros-lunar-geometry-msgs'
'ros-lunar-kdl-parser'
'ros-lunar-moveit-msgs'
'ros-lunar-octomap'
'ros-lunar-octomap-msgs'
'ros-lunar-random-numbers'
'ros-lunar-rostime'
'ros-lunar-sensor-msgs'
'ros-lunar-srdfdom'
'ros-lunar-std-msgs'
'ros-lunar-trajectory-msgs'
'ros-lunar-urdf'
'ros-lunar-visualization-msgs'
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

