Name:           ros-kinetic-moveit
Version:        0.9.7
Release:        0%{?dist}
Summary:        ROS moveit package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-moveit-commander
Requires:       ros-kinetic-moveit-core
Requires:       ros-kinetic-moveit-planners
Requires:       ros-kinetic-moveit-plugins
Requires:       ros-kinetic-moveit-ros
Requires:       ros-kinetic-moveit-setup-assistant
BuildRequires:  ros-kinetic-catkin

%description
Meta package that contains all essential package of MoveIt!. Until Summer 2016
MoveIt! had been developed over multiple repositories, where developers'
usability and maintenance effort was non-trivial. See the detailed discussion
for the merge of several repositories.

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
* Mon Jun 05 2017 Dave Coleman <dave@dav.ee> - 0.9.7-0
- Autogenerated by Bloom

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

* Sun Nov 13 2016 Dave Coleman <dave@dav.ee> - 0.9.2-1
- Autogenerated by Bloom

