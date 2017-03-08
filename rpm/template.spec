Name:           ros-jade-moveit-runtime
Version:        0.8.6
Release:        0%{?dist}
Summary:        ROS moveit_runtime package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-moveit-core
Requires:       ros-jade-moveit-planners
Requires:       ros-jade-moveit-plugins
Requires:       ros-jade-moveit-ros-manipulation
Requires:       ros-jade-moveit-ros-move-group
Requires:       ros-jade-moveit-ros-perception
Requires:       ros-jade-moveit-ros-planning
Requires:       ros-jade-moveit-ros-planning-interface
Requires:       ros-jade-moveit-ros-warehouse
BuildRequires:  ros-jade-catkin

%description
moveit_runtime meta package contains MoveIt! packages that are essential for its
runtime (e.g. running MoveIt! on robots).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Mar 08 2017 Isaac I. Y. Saito <gm130s@gmail.com> - 0.8.6-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Isaac I. Y. Saito <gm130s@gmail.com> - 0.8.5-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Isaac I. Y. Saito <gm130s@gmail.com> - 0.8.4-0
- Autogenerated by Bloom

