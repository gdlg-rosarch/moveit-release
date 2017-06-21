Name:           ros-kinetic-moveit-planners-ompl
Version:        0.9.8
Release:        0%{?dist}
Summary:        ROS moveit_planners_ompl package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-moveit-core
Requires:       ros-kinetic-moveit-ros-planning
Requires:       ros-kinetic-ompl
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-moveit-core
BuildRequires:  ros-kinetic-moveit-resources
BuildRequires:  ros-kinetic-moveit-ros-planning
BuildRequires:  ros-kinetic-ompl
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-tf

%description
MoveIt interface to OMPL

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
* Wed Jun 21 2017 Ioan Sucan <isucan@google.com> - 0.9.8-0
- Autogenerated by Bloom

* Mon Jun 05 2017 Ioan Sucan <isucan@google.com> - 0.9.7-0
- Autogenerated by Bloom

* Wed Apr 12 2017 Ioan Sucan <isucan@google.com> - 0.9.6-0
- Autogenerated by Bloom

* Sat Apr 08 2017 Ioan Sucan <isucan@google.com> - 0.9.5-1
- Autogenerated by Bloom

* Wed Mar 08 2017 Ioan Sucan <isucan@google.com> - 0.9.5-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Ioan Sucan <isucan@google.com> - 0.9.4-0
- Autogenerated by Bloom

* Wed Nov 16 2016 Ioan Sucan <isucan@google.com> - 0.9.3-0
- Autogenerated by Bloom

* Sun Nov 13 2016 Ioan Sucan <isucan@willowgarage.com> - 0.9.2-1
- Autogenerated by Bloom

