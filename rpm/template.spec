Name:           ros-kinetic-moveit-ros-benchmarks
Version:        0.9.6
Release:        0%{?dist}
Summary:        ROS moveit_ros_benchmarks package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-moveit-ros-planning
Requires:       ros-kinetic-moveit-ros-warehouse
Requires:       ros-kinetic-pluginlib >= 1.10.4
Requires:       ros-kinetic-roscpp
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-moveit-ros-planning
BuildRequires:  ros-kinetic-moveit-ros-warehouse
BuildRequires:  ros-kinetic-pluginlib >= 1.10.4
BuildRequires:  ros-kinetic-roscpp

%description
Enhanced tools for benchmarks in MoveIt!

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Apr 12 2017 Dave Coleman <dave@dav.ee> - 0.9.6-0
- Autogenerated by Bloom

* Sat Apr 08 2017 Dave Coleman <dave@dav.ee> - 0.9.5-1
- Autogenerated by Bloom

* Wed Mar 08 2017 Dave Coleman <dave@dav.ee> - 0.9.5-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Dave Coleman <dave@dav.ee> - 0.9.4-0
- Autogenerated by Bloom

* Wed Nov 16 2016 Dave Coleman <dave@dav.ee> - 0.9.3-0
- Autogenerated by Bloom

* Sun Nov 13 2016 Ryan Luna <rluna@rice.edu> - 0.9.2-1
- Autogenerated by Bloom

