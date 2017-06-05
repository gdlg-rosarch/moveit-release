Name:           ros-lunar-moveit-core
Version:        0.9.7
Release:        0%{?dist}
Summary:        ROS moveit_core package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       boost-devel
Requires:       console-bridge-devel
Requires:       eigen3-devel
Requires:       fcl-devel
Requires:       ros-lunar-eigen-conversions
Requires:       ros-lunar-eigen-stl-containers
Requires:       ros-lunar-geometric-shapes >= 0.5.2
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-kdl-parser
Requires:       ros-lunar-moveit-msgs
Requires:       ros-lunar-octomap
Requires:       ros-lunar-octomap-msgs
Requires:       ros-lunar-random-numbers
Requires:       ros-lunar-rostime
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-srdfdom
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-trajectory-msgs
Requires:       ros-lunar-urdf
Requires:       ros-lunar-visualization-msgs
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
BuildRequires:  assimp
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  eigen3-devel
BuildRequires:  fcl-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-lunar-angles
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-eigen-conversions
BuildRequires:  ros-lunar-eigen-stl-containers
BuildRequires:  ros-lunar-geometric-shapes >= 0.5.2
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-kdl-parser
BuildRequires:  ros-lunar-moveit-msgs
BuildRequires:  ros-lunar-moveit-resources
BuildRequires:  ros-lunar-octomap
BuildRequires:  ros-lunar-octomap-msgs
BuildRequires:  ros-lunar-orocos-kdl
BuildRequires:  ros-lunar-random-numbers
BuildRequires:  ros-lunar-roslib
BuildRequires:  ros-lunar-rostime
BuildRequires:  ros-lunar-rosunit
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-shape-msgs
BuildRequires:  ros-lunar-srdfdom
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf-conversions
BuildRequires:  ros-lunar-trajectory-msgs
BuildRequires:  ros-lunar-urdf
BuildRequires:  ros-lunar-visualization-msgs
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel

%description
Core libraries used by MoveIt!

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Jun 05 2017 Dave Coleman <dave@dav.ee> - 0.9.7-0
- Autogenerated by Bloom

* Fri May 12 2017 Dave Coleman <dave@dav.ee> - 0.9.6-1
- Autogenerated by Bloom

* Wed May 10 2017 Dave Coleman <dave@dav.ee> - 0.9.6-0
- Autogenerated by Bloom

