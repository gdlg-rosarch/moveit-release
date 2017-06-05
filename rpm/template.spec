Name:           ros-lunar-moveit-ros-planning-interface
Version:        0.9.7
Release:        0%{?dist}
Summary:        ROS moveit_ros_planning_interface package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       ros-lunar-actionlib
Requires:       ros-lunar-eigen-conversions
Requires:       ros-lunar-moveit-ros-manipulation
Requires:       ros-lunar-moveit-ros-move-group
Requires:       ros-lunar-moveit-ros-planning
Requires:       ros-lunar-moveit-ros-warehouse
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-tf
Requires:       ros-lunar-tf-conversions
BuildRequires:  eigen3-devel
BuildRequires:  python-catkin_pkg
BuildRequires:  python-devel
BuildRequires:  ros-lunar-actionlib
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-eigen-conversions
BuildRequires:  ros-lunar-moveit-resources
BuildRequires:  ros-lunar-moveit-ros-manipulation
BuildRequires:  ros-lunar-moveit-ros-move-group
BuildRequires:  ros-lunar-moveit-ros-planning
BuildRequires:  ros-lunar-moveit-ros-warehouse
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-tf-conversions

%description
Components of MoveIt that offer simpler interfaces to planning and execution

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
* Mon Jun 05 2017 Michael Ferguson <mferguson@fetchrobotics.com> - 0.9.7-0
- Autogenerated by Bloom

* Fri May 12 2017 Michael Ferguson <mferguson@fetchrobotics.com> - 0.9.6-1
- Autogenerated by Bloom

* Wed May 10 2017 Michael Ferguson <mferguson@fetchrobotics.com> - 0.9.6-0
- Autogenerated by Bloom

