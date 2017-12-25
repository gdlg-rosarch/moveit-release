Name:           ros-kinetic-moveit-ros-perception
Version:        0.9.11
Release:        0%{?dist}
Summary:        ROS moveit_ros_perception package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       freeglut-devel
Requires:       glew-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-moveit-core
Requires:       ros-kinetic-moveit-msgs
Requires:       ros-kinetic-octomap
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf-conversions
Requires:       ros-kinetic-urdf
BuildRequires:  eigen3-devel
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-moveit-core
BuildRequires:  ros-kinetic-moveit-msgs
BuildRequires:  ros-kinetic-octomap
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf-conversions
BuildRequires:  ros-kinetic-urdf

%description
Components of MoveIt connecting to perception

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
* Mon Dec 25 2017 Michael Ferguson <mferguson@fetchrobotics.com> - 0.9.11-0
- Autogenerated by Bloom

* Sat Dec 09 2017 Michael Ferguson <mferguson@fetchrobotics.com> - 0.9.10-0
- Autogenerated by Bloom

* Sun Aug 06 2017 Ioan Sucan <isucan@google.com> - 0.9.9-0
- Autogenerated by Bloom

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

* Sun Nov 13 2016 Ioan Sucan <isucan@google.com> - 0.9.2-1
- Autogenerated by Bloom

