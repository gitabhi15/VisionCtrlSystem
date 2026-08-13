package com.visionctrlsys.doorcam.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.visionctrlsys.doorcam.model.AccessLog;

public interface AccessLogRepository extends JpaRepository<AccessLog, Long> {

}
